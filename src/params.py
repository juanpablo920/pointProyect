class ParamServer:
    def __init__(self):
        # /home/pocampo/
        # /home/sirui/Documents/Johan_Avila/
        # /home/avila/Documentos/
        # /home/juanpablo
        self.prefix = "/home/juanpablo/"

        # example
        self.data_file = "PCD_NIR_training_4M_low50.txt"
        # self.dsp_types = ["L", "P", "S", "O", "A", "E", "C"]  # Sum
        self.dsp_types = ["P"]
