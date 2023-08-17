import React from 'react';
import NotificationManager from './NotificationManager';

class UI extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      notificationManager: new NotificationManager()
    };
  }

  render() {
    return (
      <div>
        <h1>Welcome to the AI Agent System</h1>
        <button onClick={() => this.state.notificationManager.sendAllNotifications()}>Send All Notifications</button>
        <button onClick={() => this.state.notificationManager.receiveAllUpdates()}>Receive All Updates</button>
      </div>
    );
  }
}

export default UI;