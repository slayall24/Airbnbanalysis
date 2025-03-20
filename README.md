# NYC Airbnb Data Visualization

## Project Overview
This project visualizes key insights from the **AB_NYC_2019.csv** dataset, which contains Airbnb listings data for New York City. The visualizations are created using **Plotly** and hosted as a static website on **GitHub Pages**.

## Features
- **Price Distribution**: Displays the number of listings within different price ranges (e.g., $0-$100, $101-$200, etc.).
- **Neighborhood Group Count**: Shows the number of listings in each NYC neighborhood group.
- **Price by Neighborhood**: Visualizes the average price of listings in different neighborhoods.


## Installation
To run this project locally, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nyc-airbnb-visualization.git
   cd nyc-airbnb-visualization
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install pandas plotly
   ```

4. **Run the Python script to generate visualizations**
   ```bash
   python generate_plots.py
   ```
   This will generate HTML files for each visualization.

5. **Open the HTML files in a browser**
   Simply double-click on the generated `price_distribution.html` or use a local server to preview.

## Hosting on GitHub Pages
This project is designed to be hosted as a static website on **GitHub Pages**:
1. Commit all files, including the generated HTML files.
2. Push the repository to GitHub.
3. Go to **Settings > Pages** and select the branch where the HTML files are stored.
4. Enable GitHub Pages, and your website will be live at `https://your-username.github.io/nyc-airbnb-visualization/`.

## File Structure
```
nyc-airbnb-visualization/
│── AB_NYC_2019.csv          # Dataset file
│── generate_plots.py        # Python script to generate visualizations
│── price_distribution.html  # Generated visualization (Price Distribution)
│── neighborhood_count.html  # Generated visualization (Neighborhood Count)
│── price_by_neighborhood.html  # Generated visualization (Price by Neighborhood)
│── index.html               # Main webpage to display visualizations
│── README.md                # Project documentation (this file)
```

## Technologies Used
- **Python** (Data Processing: `pandas`)
- **Plotly** (Interactive Visualizations)
- **GitHub Pages** (Static Website Hosting)

## Contributing
Feel free to fork the repository and submit pull requests for improvements or additional visualizations.

## License
This project is open-source and available under the **MIT License**.

---
_Developed by Jhanvi Shah_

