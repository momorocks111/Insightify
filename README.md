# 📊 Insightify

Insightify is an AI-powered data navigator app for analyzing files and databases, with a focus on financial and banking data. It provides an interactive interface for data exploration and analysis.

## 🌟 Features

- 📤 Data upload and analysis for various file formats (SQL dumps, CSV, etc.)
- 🤖 AI-powered analysis of database structures and content
- 📈 Detailed statistical analysis and data visualization
- 🌓 Dark/Light theme toggle
- 📱 Responsive design

## 🛠️ Tech Stack

### Frontend

- React (with Vite)
- react-flow (for schema visualization)
- react-router-dom
- react-circular-progressbar

### Backend

- Python 3.8+
- Flask
- SQLite (for data processing)
- Pandas
- NumPy
- Scikit-learn

### Styling

- Vanilla CSS

## 🚀 Getting Started

### Prerequisites

- Node.js (v14+)
- Python (3.8+)
- Git

### Installation

1. Clone the repository
2. Frontend setup:
   - Navigate to the frontend directory
   - Run `npm install`
   - Start the development server with `npm run dev`
3. Backend setup:
   - Navigate to the backend directory
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Start the Flask server: `python app.py`

## 💻 Usage

1. Open your browser and navigate to `http://localhost:5173`
2. Upload your data file (SQL dump, CSV, etc.) through the frontend interface
3. The backend will process the file and provide a comprehensive analysis
4. Explore the data structure, statistics, and visualizations in the user interface

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## 🙏 Acknowledgements

- [React Flow](https://reactflow.dev/) for the amazing graph visualization library
- [Flask](https://flask.palletsprojects.com/) for the lightweight WSGI web application framework

Made with ❤️
