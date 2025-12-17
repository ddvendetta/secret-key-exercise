# generate_diagram.py
from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import Document, InputOutput, PredefinedProcess

# This script requires the 'diagrams' library and graphviz to be installed.
# You can install them with:
# pip install diagrams
#
# On macOS, you can install graphviz with Homebrew:
# brew install graphviz
#
# On Debian/Ubuntu, you can install graphviz with apt-get:
# sudo apt-get install graphviz
#
# For other systems, please see the Graphviz installation instructions.

# Diagram 1: Overall RC4 Flow
with Diagram("RC4 Stream Cipher Flow", show=False, filename="rc4_flow_diagram", direction="LR"):
    plaintext = Document("Plaintext")
    secret_key = InputOutput("Secret Key")

    with Cluster("RC4 Encryption Process (rc4 function)"):
        # The two main algorithms within RC4
        ksa_process = PredefinedProcess("1. Key-Scheduling\nAlgorithm (KSA)")
        prga_process = PredefinedProcess("2. Pseudo-Random\nGeneration (PRGA)")
        
        # The operation that combines the keystream and plaintext
        xor_operation = PredefinedProcess("3. XOR Operation")

        # Data flow within the cluster
        secret_key >> ksa_process >> prga_process
        prga_process >> xor_operation

    ciphertext = Document("Ciphertext")

    # Connect the external inputs/outputs to the process
    plaintext >> xor_operation
    xor_operation >> ciphertext

# Diagram 2: Detailed XOR Operation
with Diagram("XOR Operation Details", show=False, filename="xor_operation_detail", direction="TB"):
    plaintext_input = InputOutput("Plaintext / Ciphertext")
    keystream_input = InputOutput("Keystream from PRGA")
    
    xor_node = PredefinedProcess("Byte-by-byte\nXOR")

    ciphertext_output = Document("Ciphertext / Plaintext")

    plaintext_input >> xor_node
    keystream_input >> xor_node
    xor_node >> ciphertext_output


print("Diagram script 'generate_diagram.py' updated successfully.")
print("Run 'python generate_diagram.py' to create two diagram files:")
print("- rc4_flow_diagram.png (Overall flow)")
print("- xor_operation_detail.png (XOR step details)")

