# Manim Bitcoin Animation Experiments

## Description

This project uses the [Manim](https://www.manim.community/) animation library to create visual explanations of various Bitcoin concepts. The animations illustrate topics such as transactions, blockchain structure, mining, and decentralization, providing a clear and engaging way to understand how Bitcoin works.

## Installation

To set up the project environment, follow these steps:

1. **Install Python**: If you don't have Python installed, download and install the latest version from [python.org](https://www.python.org/downloads/).

2. **Install Manim**: Follow the instructions on the [Manim installation guide](https://docs.manim.community/en/stable/installation.html) to install Manim and its dependencies.

   - For macOS:
     ```bash
     brew install py3cairo ffmpeg
     pip install manim
     ```

   - For Windows:
     - Install [Chocolatey](https://chocolatey.org/install).
     - Install [FFmpeg](https://ffmpeg.org/download.html) and [Cairo](https://www.cairographics.org/download/):
       ```bash
       choco install ffmpeg cairo
       ```
     - Install [LaTeX](https://miktex.org/download) (MiKTeX recommended).
     - Install Manim:
       ```bash
       pip install manim
       ```

   - For Linux (Ubuntu/Debian):
     ```bash
     sudo apt update
     sudo apt install ffmpeg libcairo2-dev libpango1.0-dev
     pip install manim
     ```

3. **Clone the repository** (if applicable):

   ```bash
   git clone [repository URL]
   cd [repository directory]
   ```

4. **Install additional dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate the Bitcoin animation, run the `main.py` script from the command line:

```bash
manim main.py BitcoinExplanation -p -ql
```

This command will:

- Run the `BitcoinExplanation` scene defined in `main.py`.
- Open a preview of the animation (`-p` flag).
- Render the animation in low quality (`-ql` flag). You can change this to `-qh` for high quality or `-qk` for 4K.

The output animation will be saved in the `media/videos/main/` directory.

## Animation Details

The animation consists of the following sections:

### Transactions and Blocks

This section demonstrates how Bitcoin transactions are created and added to blocks. It shows an example transaction between Alice and Bob, where Alice sends 1 BTC to Bob. The transaction is then represented as a data structure containing the sender, receiver, and amount.

### Blockchain Structure

This part illustrates the structure of the blockchain, showing how blocks are linked together using cryptographic hashes. It visualizes a chain of three blocks, each containing a block number, hash, and previous hash.

### Mining & Proof-of-Work

This section explains the concept of mining and proof-of-work. It shows a block with data and a nonce, and demonstrates how miners try to find a nonce that produces a valid hash (starting with a certain number of zeros).

### Decentralized Network

This part visualizes the decentralized nature of the Bitcoin network. It shows multiple nodes connected to each other, representing how transactions and blocks are propagated across the network.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m "Add your commit message"`
4. Push your changes to your fork: `git push origin feature/your-feature-name`
5. Create a pull request to the main repository.

Please report any issues or suggest improvements by opening an issue on the [issue tracker]([repository URL]/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
