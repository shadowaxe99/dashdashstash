import Notification from './Notification';

class NotificationManager {
  constructor() {
    this.notifications = [];
  }

  addNotification(message, type) {
    const notification = new Notification(message, type);
    this.notifications.push(notification);
  }

  removeNotification(index) {
    this.notifications.splice(index, 1);
  }

  sendAllNotifications() {
    this.notifications.forEach((notification, index) => {
      try {
        notification.sendNotification();
        this.removeNotification(index);
      } catch (error) {
        console.error(`Failed to send notification: ${error}`);
      }
    });
  }

  receiveAllUpdates() {
    this.notifications.forEach((notification, index) => {
      try {
        notification.receiveUpdate();
        this.removeNotification(index);
      } catch (error) {
        console.error(`Failed to receive update: ${error}`);
      }
    });
  }
}

export default NotificationManager;