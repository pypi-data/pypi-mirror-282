from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters

class Calculator:
    def __init__(self):
        # Start Py4J gateway server
        self.gateway = JavaGateway(
            gateway_parameters=GatewayParameters(port=25333),
            callback_server_parameters=CallbackServerParameters(),
            python_server_entry_point=self
        )

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Entry point for starting the Py4J gateway server
def start_gateway():
    calculator = Calculator()

# Ensure the gateway server is started when this script is run
if __name__ == "__main__":
    start_gateway()