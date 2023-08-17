class Notification {
  constructor(message, type) {
    this.message = message;
    this.type = type;
  }

  sendNotification() {
    // Logic for sending the notification goes here
    console.log(`Sending ${this.type} notification: ${this.message}`);
  }

  receiveUpdate() {
    // Logic for receiving an update goes here
    console.log(`Received ${this.type} update: ${this.message}`);
  }
}

export default Notification;