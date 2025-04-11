import logging
from client_OPC_UA import client_OPC_UA


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(filename)s - '
        '%(funcName)s - %(message)s'
    )
    logger = logging.getLogger("demo_read_boolean")

    # Prompt user for server URL, namespace, and node ID
    server_url = input("Enter the OPC UA server URL: ")
    namespace = int(input("Enter the namespace of the node: "))
    node_id = int(input("Enter the node ID: "))

    # Initialize the client
    opcua_client = client_OPC_UA(p_URL=server_url, p_retry_attempts=5,
                                 p_retry_delay=2)

    # Connect to the server
    connection_result = opcua_client.connect()
    if (connection_result.success):
        logger.info("Connected to the OPC UA server successfully.")
    else:
        logger.error(f"Failed to connect: {connection_result.error}")
        return

    # Read a boolean value from the node
    read_result = opcua_client.read_value(namespace, node_id)
    if (read_result.success):
        logger.info(f"Read value: {read_result.value} "
                    f"(Type: {read_result.node_type}) from node "
                    f"ns={namespace};i={node_id}.")
    else:
        logger.error(f"Failed to read value: {read_result.error}")

    # Disconnect from the server
    opcua_client.disconnect()
    logger.info("Disconnected from the OPC UA server.")


if __name__ == "__main__":
    main()
