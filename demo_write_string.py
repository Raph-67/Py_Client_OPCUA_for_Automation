import logging
from client_OPC_UA import client_OPC_UA


def main():
    # Configure logging for the program
    program_logger = logging.getLogger("program_logger")
    program_logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(filename)s - '
        '%(funcName)s - %(message)s'
    ))
    program_logger.addHandler(handler)

    # Prompt user for server URL, namespace, and node ID
    program_logger.info("Starting the OPC UA write demo.")
    server_url = input("Enter the OPC UA server URL: ")
    namespace = int(input("Enter the namespace of the node: "))
    node_id = int(input("Enter the node ID: "))
    value_to_write = input("Enter the string value to write: ")

    # Initialize the client
    opcua_client = client_OPC_UA(p_URL=server_url, p_retry_attempts=5,
                                 p_retry_delay=2)

    # Connect to the server
    connection_result = opcua_client.connect()
    if connection_result.success:
        program_logger.info("Connected to the OPC UA server successfully.")
    else:
        program_logger.error(f"Failed to connect: {connection_result.error}")
        return

    # Write the string value to the node
    write_result = opcua_client.write_value(namespace, node_id, value_to_write)
    if write_result.success:
        program_logger.info(f"Value '{value_to_write}' written successfully to"
                            f" node ns={namespace};i={node_id}.")
    else:
        program_logger.error(f"Failed to write value: {write_result.error}")

    # Disconnect from the server
    opcua_client.disconnect()
    program_logger.info("Disconnected from the OPC UA server.")


if __name__ == "__main__":
    main()
