# WorkOutTracking API

WorkOutTracking API is a Python script designed to help users track their daily workouts and log them in a Google Sheet for easy monitoring. By integrating with the Nutritionix API, the script retrieves exercise data and calculates calories burned. The Sheety API is used to store the workout logs efficiently.

## Features

- **Exercise Tracking**: Automatically calculates calories burned and logs workout details based on user input.
- **API Integration**:
  - **Nutritionix API**: Fetch exercise data, including calories burned, based on user input.
  - **Sheety API**: Log workout details, such as duration, calories burned, and type of exercise, into a Google Sheet.
- **Data Logging**: Stores workout information, making it accessible and easy to monitor progress.
- **Dynamic Inputs**: Supports multiple exercise types entered in a single session.

## Technologies Used

- **Programming Language**: Python
- **APIs**:
  - Nutritionix API
  - Sheety API
- **Libraries**:
  - `requests` for API communication.
  - `datetime` for managing timestamps.

## Setup and Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/PabloSimonEstrada/WorkOutTraking.git
   cd WorkOutTraking
   ```

2. **Install Dependencies**  
   Ensure Python is installed on your system. Install required libraries using:
   ```bash
   pip install requests
   ```

3. **Set Up API Keys**  
   - Obtain API keys for:
     - [Nutritionix](https://www.nutritionix.com/business/api)
     - [Sheety](https://sheety.co/)
   - Open the script and update the following variables with your API credentials:
     ```python
     NUTRITIONIX_APP_ID = "your_app_id"
     NUTRITIONIX_API_KEY = "your_api_key"
     SHEETY_ENDPOINT = "your_sheety_endpoint"
     ```

4. **Run the Script**  
   Execute the script to log your workout:
   ```bash
   python workout_tracker.py
   ```

## Usage

1. **Log Workouts**  
   - Input your workout details, such as:
     ```
     Ran 5 kilometers and cycled for 20 minutes
     ```
   - The script fetches data for each activity and logs them in your Google Sheet.

2. **Monitor Logs**  
   - Access your Google Sheet to view the recorded details, including:
     - Date
     - Exercise type
     - Duration
     - Calories burned

## Example Output

When you log your workout, the script outputs:
```bash
Workout data logged successfully:
Date: 2024-11-20
Exercise: Running
Duration: 30 minutes
Calories: 250 kcal
```

## Future Enhancements

- Add a graphical interface for easier interaction.
- Include weekly and monthly workout summaries.
- Integrate with wearable fitness devices for automatic logging.

## Contribution

Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues to improve the project.
