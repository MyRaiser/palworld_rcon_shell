from rcon.source import Client
from rcon.source.proto import Packet


class MyClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def run(self, command: str, *args: str, encoding: str = "utf-8") -> str:
        """Run a command."""
        request = Packet.make_command(command, *args, encoding=encoding)
        response = client.communicate(request)
        # request/response id check here is removed
        return response.payload.decode(encoding)


if __name__ == "__main__":
    # REPL
    with MyClient("localhost", 25575, passwd="whosyourdaddy") as client:
        while True:
            try:
                command = input(">>> ").strip()
                if not command.startswith("/"):
                    continue
                    
                response = client.run(*command.removeprefix("/").split())
                print(response)

            except KeyboardInterrupt:
                print("\nKeyboard Interrupt")
                break
            
            except Exception as e:
                print(f"Exception: {e}")
                break
