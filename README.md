# IPTV-Search

IPTV-Search is a Python program that allows you to search for channels in the IPTV database CSV file hosted on GitHub. It retrieves channel information based on the provided keyword and filters out repeated results. The program provides the name, language, categories, and NSFW flag of the matching channels along with their respective links.

## Requirements

- Python 3.x
- csv module
- requests module

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/lopekinz/IPTV-Search.git
   ```

2. Navigate to the repository directory:

   ```shell
   cd IPTV-Search
   ```

3. Install the required modules:

   ```shell
   pip install csv requests
   ```

4. Run the program:

   ```shell
   python IPTV-Search.py
   ```

5. Enter a keyword to search for in the IPTV database.

6. The program will display the unique channels that match the keyword, along with their name, language, categories, NSFW flag, and link.

## Example

Searching for the keyword "news" will display the following output:

```
Name: CNN
Language: English
Categories: News
Is NSFW: No
Website: https://www.cnn.com

Name: BBC World News
Language: English
Categories: News
Is NSFW: No
Website: https://www.bbc.com/news

...
```

## Credits

- This program utilizes the IPTV database hosted on [GitHub](https://github.com/iptv-org/database).

## License

This project is licensed under the [MIT License](LICENSE).
