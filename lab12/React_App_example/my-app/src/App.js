import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import PostList from "./components/PostList";
import PostCreate from "./components/PostCreate";
import Home from "./components/Home";
import styles from '../src/App.module.css';

const App = () => {
  return (
    <Router>
      <div className={styles.container}>
        <h1>React Post App</h1>
        <nav>
          <div><Link className={styles.navLink} to="/">Home</Link></div>
          <div><Link className={styles.navLink} to="/posts">Posts</Link></div>
        </nav>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/posts" element={<PostList />} />
          <Route exact path="/posts/create" element={<PostCreate />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;