import React, { useEffect, useState } from 'react'; 
import axios from 'axios'; 
import { Link } from 'react-router-dom'; 
import styles from '../components/PostList.module.css'; 
 
const PostList = () => { 
    const [posts, setPosts] = useState([]);   
    useEffect(() => { 
      fetchPosts(); 
    }, []); 
    const fetchPosts = async () => { 
      try { 
        const response = await axios.get('http://localhost:8000/posts/'); 
        setPosts(response.data); 
        console.log(response.data); 
      } catch (error) { 
        console.error(error); 
      } 
    }; 
    return ( 
      <div className={styles.wraper}> 
       <h1 className={styles.header}>Posts</h1>   
          {posts.map((post) => (         
            <div className={styles.post} key={post.id}> 
              <div className={styles.postTitle}> 
                {post.title} 
              </div> 
              <div className={styles.postContent}> 
                {post.content} 
              </div> 
            </div> 
          ))}   
        <div className={styles.buttons}> 
          <Link className={styles.createNew} to="/posts/create">Create New Post</Link> 
          <Link className={styles.createNew} to="/">Main page</Link> 
        </div> 
      </div> 
    ); 
  }; 
  
  export default PostList;