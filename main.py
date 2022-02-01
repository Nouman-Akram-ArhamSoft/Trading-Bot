import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("7e18d054011ee2662e61ac90435a3bf82837909e672692536fdf70fa46f31a26",
                            "50439ab15e6d73e2a7dc86685caed35a60b115cde3e8d829c4da35c8a83a2ed3",
                            testnet=True, futures=True)
    bitmex = BitmexClient(
        "RDhtbbdQz1rp7MXsFJFs5Rb4",
        "uG75h7wzk3_-AaWVRGB1NerkIPY4IX5uoQZ4Jobs4mex`xdA6J4",
        testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
