from plyer import notification
import time

class Popups:
    def __init__(self, title="Notification", message="Default message", timeout=5):
        self.title = title
        self.message = message
        self.timeout = timeout

    def show_notification(self):
        notification.notify(
            title=self.title,
            message=self.message,
            timeout=self.timeout
        )

if __name__ == "__main__":
    # Example usage
    popup = Popups(title="My App", message="Hello, World!", timeout=5)
    popup.show_notification()

    # Give some time to display the notification
    time.sleep(10)  # Adjust the sleep duration as needed