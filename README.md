# IDS/IPS with Machine Learning

This project implements an Intrusion Detection and Prevention System (IDS/IPS) using Machine Learning. The system captures network packets, extracts features, trains a machine learning model, and provides a web interface for real-time predictions.

## Project Structure
- `capture_packets.py`: Captures network packets and saves them to a CSV file.
- `feature_extraction.py`: Extracts features from captured packets.
- `preprocess_data.py`: Preprocesses the feature data.
- `train_model.py`: Trains a machine learning model.
- `app.py`: Flask web application for making predictions.

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/IDS_IPS_ML.git
    cd IDS_IPS_ML
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the packet capture script:
    ```bash
    python capture_packets.py
    ```

4. Run the feature extraction script:
    ```bash
    python feature_extraction.py
    ```

5. Run the data preprocessing script:
    ```bash
    python preprocess_data.py
    ```

6. Train the machine learning model:
    ```bash
    python train_model.py
    ```

7. Run the Flask web application:
    ```bash
    python app.py
    ```

## Usage
Send a POST request to the `/predict` endpoint with the following JSON structure:
```json
{
  "time_diff": 0.005,
  "packet_size": 1500,
  "proto": "TCP"
}
```
## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
