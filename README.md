# Google Play Store Scraper

Google Play Store Scraper is a Python-based tool that allows users to extract data from the Google Play Store. This tool scrapes app details and reviews for any application available on the platform and provides a detailed sentiment analysis of the reviews.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **App Details Scraping**: Extracts detailed information about apps, including name, description, developer, category, size, and version.
- **Review Scraping**: Collects user reviews and ratings for any app.
- **Sentiment Analysis**: Provides a detailed sentiment analysis of the scraped reviews.
- **Configurable Output**: Save the scraped data and analysis in various formats like JSON, CSV, or Excel.

## Installation

To get started with the Google Play Store Scraper, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/abdul-28930/googleplaystorescraper.git
    cd googleplaystorescraper
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Scraper**:

    To start scraping and analyzing an app, run the following command and provide the app link when prompted:

    ```bash
    python scraper.py
    ```

    The script will ask you to enter the URL of the app you want to scrape from the Google Play Store. For example:

    ```
    Enter the Google Play Store app URL: https://play.google.com/store/apps/details?id=com.android.chrome
    ```

    The tool will then scrape the app's details and reviews and perform a sentiment analysis on the reviews.

2. **Output Options**:

    - The scraped data and sentiment analysis results will be saved in the specified format (JSON, CSV, Excel) and directory.
  
    Example command with output format option:

    ```bash
    python scraper.py --output_format csv
    ```

## Dependencies

- Python 3.6 or higher
- Requests
- BeautifulSoup
- pandas
- lxml
- nltk (Natural Language Toolkit for sentiment analysis)

To install these dependencies, run:

```bash
pip install requests beautifulsoup4 pandas lxml nltk
```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please reach out to the project maintainer at:

- Abdul - [GitHub Profile](https://github.com/abdul-28930)
