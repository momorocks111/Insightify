# Insightify

Insightify is an AI-powered data navigator app used for analyzing data in files and databases. It provides an interactive interface for data exploration and analysis, with a focus on financial and banking data.

## Features

- Data upload and analysis for various file formats, including SQL dumps
- AI-powered analysis of database structures and content
- Detailed statistical analysis and data visualization preparation
- Dark/Light theme toggle
- Responsive design

## Tech Stack

- Frontend: React with Vite
- Backend: Python with Flask
- Database: SQLite (for data processing)
- Machine Learning: Scikit-learn
- Data Processing: Pandas, NumPy
- Styling: Vanilla CSS

## Getting Started

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

## Usage

1. Upload your data file (SQL dump, CSV, etc.) through the frontend interface
2. The backend will process the file and provide a comprehensive analysis
3. Explore the data structure, statistics, and visualizations in the user interface

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
