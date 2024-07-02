import time
import pyvisa
import os
import logging

out_channels = {1: 'OUT1', 2: 'OUT2', 3: 'OUT3', 4: 'OUT4'}


class HMP4040_Psu:
    """
    ``Base class for the Rohde & Schwarz HMP4040 PSU``
    """
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    def __init__(self, connection_string=None):
        if not connection_string:
            self.connection_string = os.getenv("HMP_CONNECTION_STRING", default="TCPIP::192.168.1.128::5025::SOCKET")
        else:
            self.connection_string = connection_string
        self.resource_manager = None

    def open_connection(self):
        """
         ``Opens a TCP/IP connection to connect to the Rohde & Schwarz HMP4040 PSU`` \n
        """
        self.resource_manager = pyvisa.ResourceManager()
        try:
            self.hmp = self.resource_manager.open_resource(self.connection_string)
            self.hmp.read_termination = '\n'
            self.hmp.write_termination = '\n'
            logging.info(f": Opening PSU Resource at {self.connection_string}")
        except Exception as e:
            raise Exception(f": ERROR {e}: Could not open Resource")

    def close_connection(self):
        """
        ``Closes the TCP/IP connection to the R&S HMP4040 PSU`` \n
        """
        logging.info(f": Closing connection")
        self.resource_manager.close()

    def self_test(self):
        """
        ``Performs the self-test and checks for system errors`` \n
        :return: `bool` : True or Error
        """
        sys_err = str(self.hmp.query(f'SYST:ERR?', delay=1))
        if sys_err == '0, "No error"':
            try:
                selftest = self.hmp.query(f'*TST?', delay=1)
                if selftest == "0":
                    logging.info(": PASS: SELF-TEST PASSED!")
                    return True
                else:
                    logging.error(f"Self-test FAILED")
                    return False
            except Exception as e:
                raise Exception(f": ERROR: {e} One or more self-test has FAILED")
        else:
            logging.error(f": SYSTEM_ERROR: {sys_err}")
            raise Exception(f": {sys_err}")

    def id_number(self):
        """
        ``This function returns the ID number of the device`` \n
        :return: `str` : ID number
        """
        time.sleep(5)
        idn = self.hmp.query(f'*IDN?', delay=2)
        logging.info(f": IDN: {idn} \n")
        return str(idn)

    def scpi_version(self):
        """
        ``This function gets the SCPI version info for the R&S HMP4040 PSU`` \n
        :return: `str` : SCPI version number
        """
        scpi_ver = self.hmp.query(f'SYST:VERS?', delay=1)
        logging.info(f": SCPI Version: {scpi_ver}")
        return str(scpi_ver)

    def set_remote(self):
        """
        ``This function set the R&S HMP4040 PSU to a remote status`` \n
        :return: None
        """
        self.hmp.write(f'SYST:REM')
        logging.info(f": System is set to REMOTE")

    def channel_selection(self, channel):
        """
        ``This function selects the output channel`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :return: `bool` : True or False
        """
        self.hmp.write(f'INST:NSEL {channel}')
        channel_selection = self.hmp.query(f'INST:NSEL?')
        if channel_selection == str(channel):
            logging.info(f": Channel {channel} is selected.")
            return True
        else:
            logging.info(f": ERROR: Failed to select channel {channel} ")
            return False

    def set_voltage(self, channel, volt_in):
        """
        ``This function sets the output voltage for the R&S HMP4040 PSU`` \n
        :param volt_in: `int` : Voltage in the range of 0-1200 Volts \n
        :param channel: `int` : Output channel out of 4 (OUT1, OUT2, OUT3, OUT4) \n
        :return: `bool` : True or raises Error
        """
        # Enables PSU output setting
        sys_err = str(self.hmp.query(f'SYST:ERR?', delay=1))
        if sys_err == '0, "No error"':
            try:
                if self.channel_selection(channel):
                    self.hmp.write(f'VOLT {volt_in}')
                    voltage = self.hmp.query(f'VOLT?')
                    if voltage is not None:
                        logging.info(f": Output Voltage Set to : {voltage} Volts")
                        return True
                    else:
                        logging.error(f"ERROR: Could not set voltage")
                        return False
            except Exception as e:
                raise Exception(f"FAIL: to set Voltage : {e}")

    def switch_on_select_output(self, channel):
        """
        Activates the voltage output on selected output channel
        :param channel: int: selected output channel out of 4
        :return: float: Minimum Voltage in Volts
                 str  : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            self.hmp.write(f'INST {out_channels[channel]}')
            self.hmp.write(f'OUTP:SEL 1')
            self.hmp.write(f'OUTP 1')
            resp = self.hmp.query(f'OUTP?')
            logging.info(resp)
            if resp == '1':
                logging.info(f": Channel {channel} turned ON ")
                return True
            else:
                logging.info(f": ERR: Cannot turn on Channel {channel} ")
                return False
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def activate_channel(self, channel):
        """
        Activates the voltage output on selected output channel
        :param channel: int: selected output channel out of 4
        :return: str  : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            self.hmp.write(f'INST {out_channels[channel]}')
            self.hmp.write(f'OUTP:SEL 1')
            logging.info(f": Channel {channel} selected ")
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def deactivate_channel(self, channel):
        """
        Activates the voltage output on selected output channel
        :param channel: int: selected output channel out of 4
        :return: str  : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            self.hmp.write(f'INST {out_channels[channel]}')
            self.hmp.write(f'OUTP:SEL 0')
            logging.info(f": Channel {channel} deselected. ")
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def on_all_outputs(self):
        """
        Activates the voltage output on selected output channel
        :return: str  : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            self.hmp.write(f'OUTP:GEN 1')
            logging.info(f": All channels turned ON ")
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def off_all_outputs(self):
        """
        Deactivates the voltage output on selected output channel
        :return: str  : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            self.hmp.write(f'OUTP:GEN 0')
            logging.info(f": All channels turned OFF ")
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def get_voltage(self, channel):
        """
        ``This function returns the output voltage of a channel`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :returns: - `float` : Output Voltage in Volts \n
                  - `str` : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            if self.channel_selection(channel):
                get_volt = self.hmp.query(f':VOLT?')
                logging.info(f": Output Voltage: {get_volt} V on channel: {channel}")
                return float(get_volt)
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def set_max_voltage(self, channel):
        """
        ``Sets the voltage to maximum voltage`` \n
        :param channel: `int` : selected output channel out of 4 \n
        :return: `bool` : True or False
        """
        if self.channel_selection(channel):
            self.hmp.write(f'VOLT MAX')
            if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
                logging.info(f": Output set to MAX voltage")
                return True
            else:
                logging.info(f": ERROR: Failed to set MAX voltage")
                return False

    def set_min_voltage(self, channel):
        """
        ``Sets the voltage to minimum voltage`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :return: `bool` : True or False
        """
        if self.channel_selection(channel):
            self.hmp.write(f'VOLT MIN')
            if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
                logging.info(f": Output set to MIN voltage")
                return True
            else:
                logging.info(f": ERROR: Failed to set MIN voltage")
                return False

    def get_max_voltage(self, channel):
        """
        ``Queries the upper limit of the output voltage`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :returns: - `float` : Maximum Voltage in Volts \n
                  - `str` : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            if self.channel_selection(channel):
                max_volt = self.hmp.query(f'VOLT? MAX')
                logging.info(f": Max Voltage: {max_volt} V on channel: {channel}")
                return float(max_volt)
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def get_min_voltage(self, channel):
        """
        ``Queries the lower limit of the output voltage`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :returns: - `float`: Minimum Voltage in Volts \n
                  - `str` : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            if self.channel_selection(channel):
                min_volt = self.hmp.query(f'VOLT? MIN')
                logging.info(f": Min Voltage: {min_volt} V on channel: {channel}")
                return float(min_volt)
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def set_current(self, channel, curr_in):
        """
        ``This function selects a channel and sets the current for the R&S HMP4040 PSU`` \n
        :param curr_in: `int` : Current in the range of 0-10 Amps \n
        :param channel: `int` : Output channel out of 4 (OUT1, OUT2, OUT3, OUT4) \n
        :returns: `bool` : True or raises Error
        """
        # Enables PSU output setting
        sys_err = str(self.hmp.query(f'SYST:ERR?', delay=1))
        if sys_err == '0, "No error"':
            try:
                if self.channel_selection(channel):
                    self.hmp.write(f'CURR {curr_in}')
                    current = self.hmp.query(f'CURR?')
                    if current is not None:
                        logging.info(f": Output Current Set to : {current} Amps")
                        return True
                    else:
                        logging.error(f"FAIL: Could not set Current")
                        return False
            except Exception as e:
                raise Exception(f"ERROR: {e}")

    def get_current(self, channel):
        """
        ``This function queries the current of a selected channel`` \n
        :param channel: Selected output channel out of 4 \n
        :returns: - `float` : Output current in Amps \n
                  - `str` : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            if self.channel_selection(channel):
                get_curr = self.hmp.query(f':CURR?')
                logging.info(f": Output current: {get_curr} A on channel: {channel}")
                return float(get_curr)
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def get_max_current(self, channel):
        """
        ``Queries the upper limit of the output current`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :returns: - `float` : Maximum current in Amps \n
                  - `str` : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            if self.channel_selection(channel):
                max_curr = self.hmp.query(f'CURR? MAX')
                logging.info(f": Max current: {max_curr} A on channel: {channel}")
                return float(max_curr)
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

    def get_min_current(self, channel):
        """
        ``Queries the lower limit of the output current`` \n
        :param channel: `int` : Selected output channel out of 4 \n
        :returns: - `float` : Minimum current in Amps \n
                  - `str` : System Error code
        """
        if self.hmp.query(f'SYST:ERR?') == '0, "No error"':
            if self.channel_selection(channel):
                min_curr = self.hmp.query(f'VOLT? MIN')
                logging.info(f": Min current: {min_curr} A on channel: {channel}")
                return float(min_curr)
        else:
            logging.info(f": System Errors: {self.hmp.query(f'SYST:ERR?')}")
            return str(self.hmp.query(f'SYST:ERR?'))

