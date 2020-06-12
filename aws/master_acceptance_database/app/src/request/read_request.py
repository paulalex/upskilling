import request_controller as controller


def lambda_handler(event, context):
    dir(controller)
    return controller.read()

if __name__ == "__main__":
    print(lambda_handler({}, {}))

