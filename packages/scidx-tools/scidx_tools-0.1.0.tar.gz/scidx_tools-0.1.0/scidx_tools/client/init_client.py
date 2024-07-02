from threading import Event

class sciDXToolsClient:
    """
    A client to interact with the sciDX REST API.

    Parameters
    ----------
    api_url : str
        The base URL of the sciDX REST API.

    Attributes
    ----------
    api_url : str
        The base URL of the sciDX REST API.
    """
    
    def __init__(self, api_url: str):
        """
        Initialize the sciDXClient with the API URL.

        Parameters
        ----------
        api_url : str
            The base URL of the external API.
        """
        self.api_url = api_url
        self._stop_event = Event()
        self._messages = []
        self._consumer_task = None
        self._loop = None
