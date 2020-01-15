import React from 'react';
import logo from './logo.svg';
import './App.css';
import ReactHLS from 'react-hls';


const TEST = ''
 
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ReactHLS url={TEST} />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
