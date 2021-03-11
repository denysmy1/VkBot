from main import Server
import vk_api

api_token = "6b9cfe86ab1f7af0f38d3664625a2205cc31ccb7ce1d031429cba053110e5341e7254983fc2475bfce9a7"

server1 = Server(api_token, #айди группы, "server1")
while True:
    try:
        server1.start()
    except vk_api.ApiError as e:
        print(e)
    except EOFError as e:
        print(e)
    except OSError as e:
        print(e)
