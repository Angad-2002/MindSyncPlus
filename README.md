# MindSyncPlus

MindSyncPlus is a web-based application designed to aid in detecting the stage of Alzheimer’s disease from MRI scans. The system integrates custom-built deep learning models with an intuitive user interface to provide accurate, stage-specific diagnoses and insights into Alzheimer’s progression.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Model Architectures](#model-architectures)
- [Model Performance](#model-performance)
- [Screenshots and Video](#screenshots-and-video)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Accurate Diagnosis**: Achieves 85%+ accuracy in identifying Alzheimer’s stages from MRI scans.
- **User-Friendly Interface**: Simplifies the process for uploading scans and obtaining predictions.
- **Data Visualization**: Provides visual insights for better understanding of model predictions.
- **Modular Design**: Built with scalability in mind to accommodate future enhancements.

## Technologies Used

- **Programming Language:** Python
- **Frameworks and Libraries:**
  - Backend: Flask
  - Frontend: HTML5, CSS3, JavaScript, Bootstrap
  - Machine Learning: TensorFlow, NumPy, Pandas, Scikit-learn
- **Database:** MySQL
- **Developer Tools:** VS Code, Jupyter Notebooks, Google Colab

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Angad-2002/MindSyncPlus.git
   ```

2. Navigate to the project directory:
   ```bash
   cd MindSyncPlus
   ```

3. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate    # For Windows
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the database:
   - Create a MySQL database.
   - Update the database credentials in the `config.py` file.

6. Run the application:
   ```bash
   python app.py
   ```

7. Access the application in your browser at `http://127.0.0.1:5000`.

## Usage

1. **Upload MRI Scans**: Navigate to the upload section and select the MRI scans you want to analyze.
2. **Analyze Results**: The system will predict the stage of Alzheimer’s and display the results.
3. **Visual Insights**: Explore detailed visualizations of the analyzed data.
4. **Manage Records**: Use the database to store and retrieve past analyses.

## Model Details

The application uses three different deep learning models to analyze MRI scans:

1. **Inception V3**:
   - Pre-trained on the ImageNet dataset.
   - Fine-tuned to classify Alzheimer’s stages.
   - Known for its efficiency and accuracy in image classification tasks.

2. **VGG19**:
   - Another pre-trained model from the ImageNet family.
   - Fine-tuned for Alzheimer’s stage detection.
   - Excels in handling deep hierarchical feature representations.

3. **Custom Model**:
   - A custom-built convolutional neural network (CNN) tailored for this project.
   - Designed with layers optimized for detecting patterns specific to Alzheimer’s MRI scans.
   - Balances performance and computational efficiency for deployment.

## Model Architectures

### 1. Inception V3
- **Architecture**:
  - Consists of inception modules that use convolutional filters of different sizes in parallel.
  - Includes auxiliary classifiers for better gradient flow.
  - Employs factorized convolutions to reduce computational cost.

### 2. VGG19
- **Architecture**:
  - Contains 19 layers: 16 convolutional layers and 3 fully connected layers.
  - Uses 3x3 filters with stride 1 and same padding.
  - Focuses on deep and uniform architecture with a fixed convolutional window.

### 3. Custom CNN Model
- **Architecture**:
  - Input Layer: Accepts MRI scans in a standardized format.
  - Convolutional Layer 1: 64 filters, 3x3 kernel, ReLU activation.
  - MaxPooling Layer 1: 2x2 pooling window.
  - Convolutional Layer 2: 64 filters, 3x3 kernel, ReLU activation.
  - MaxPooling Layer 2: 2x2 pooling window.
  - Flatten Layer: Converts 2D matrix to 1D vector.
  - Dense Layer 1: 128 units, ReLU activation.
  - Dropout Layer: 50% dropout to reduce overfitting.
  - Output Layer: 4 units with softmax activation for multi-class classification.

### Diagram

```plaintext
Input Image
    |
Conv2D (64 filters, 3x3) -> ReLU -> MaxPooling (2x2)
    |
Conv2D (64 filters, 3x3) -> ReLU -> MaxPooling (2x2)
    |
Flatten
    |
Dense (128 units) -> ReLU -> Dropout (50%)
    |
Dense (4 units) -> Softmax
```

## Model Performance

- **Accuracy:** 85%+
- **Metrics:** Evaluated using precision, recall, F1-score, and confusion matrix.
- **Dataset:** Trained on publicly available Alzheimer’s MRI datasets, with preprocessing to ensure data quality.

## Screenshots and Video

### Screenshots

1. **Home Page**:

   ![image](https://github.com/user-attachments/assets/3fbdb13c-ae1d-4c5f-bd67-a3fefd4a4dd2)

2. **Upload Section**:
   
   ![image](https://github.com/user-attachments/assets/a502b76e-0827-4690-9240-d669b4f264f6)
   ![image](https://github.com/user-attachments/assets/9d57368b-0f9e-4657-9bf1-c92a63fc1a0a)

3. **Sign-Up/Login Page**:
   
   ![image](https://github.com/user-attachments/assets/0066e79d-92da-4329-b921-b309bf839ff1)

4. **Results Page**:

   ![image](https://github.com/user-attachments/assets/596fa32d-bf2b-4481-8dce-7b3039c6d76f)

### Video Demo

A video walkthrough demonstrating the application’s functionality is available. 
[![Watch the Video Demo](https://img.youtube.com/vi/A7GCzD2R4C0/maxresdefault.jpg)](https://youtu.be/A7GCzD2R4C0)


## Future Enhancements

- Integrate additional deep learning models to improve accuracy.
- Support for other neurodegenerative diseases.
- Implement role-based access control for enhanced security.
- Add cloud storage support for MRI scans and results.

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

### Contributors
- **Ashish** [GitHub](https://github.com/Angad-2002)
- **Siddharth** [GitHub](https://github.com/Angad-2002)
- **Angad Singh** [GitHub](https://github.com/Angad-2002)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Maintainer:** Angad Singh  
[GitHub](https://github.com/Angad-2002) | [LinkedIn](https://linkedin.com/in/angad2002)

