https://static.fullstack-bootcamp.com/module-1/hero-bg.jpg

*{
    margin: 0;
    padding: 0;
    box-sizing:border-box;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    color: #39a6b2;
  }
  header{
      padding: 20px 35px;
  background-color: #39a6b2;    
  }
  header h1{
      font-weight: bold;
      font-size: 36px;
      color: #fce138;
      margin: 0;
      display: inline;
  }
  header a{
      color:#fce138;
      text-decoration: none;
  }
  header nav{
      float:right;
      margin:7px 0;
  }
  header nav ul li{
      display:inline;
  }
  header nav ul li a{
      font-weight: lighter;
      font-size: 22px;
      margin: 0 30px;
  }
  footer{
  background-color: #fce138;   
  width:100%;
  padding: 40px 35px; 
  }
  footer h2{
      display: inline;
      color:#024e76;
      font-size: 30px;
      margin: 0;
  }
  footer div {
    float: right;
    line-height: 1.5;
    text-align: right;
  }
  footer a{
      color:#024e76;
  }
  section{
      padding: 60px;
     
  }
  /* Hero Style Start */
.hero {
    background-image: url("https://static.fullstack-bootcamp.com/module-1/hero-bg.jpg");
    height: 600px;
    background-size: cover;
    background-position: center;
  }
  .hero-form{
    background: #fce138;
    padding: 20px;
    width: 500px;
    color:#024e76;
    border:#024e76 3px solid;
  position: absolute;
  bottom: 120px;
  right: 140px;
}
.hero-form p{
    margin: 5px 0 15px 0;
}
.form-input{
    border: 1px solid #024e76;
    display: block;
    padding:7px 15px;
    font-size: 16px;
  color: #024e76;
  width: 100%;
  margin-bottom: 15px;
}
.hero-form label{
    margin: 0 5px;
}
.hero-form button{
    color:#fce138;
    background-color: #024e76;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
}
  /* Hero Style End */
  .intro{
      text-align: center;
  }
  .intro h2{
      
  }
  .intro p{
      line-height: 1.7;
      color:#39a6b2;
      width: 80%;
      font-size: 20px;
      margin:0 auto;
  }
  .steps{
      text-align: center;
      background: #fce138;
  }
  .steps h2{
      
  }
  .section-title{
      font-size: 55px;
      color:#024e76;
      margin-bottom: 35px;
      padding: 0 100px 20px 100px;
      border-bottom: 3px solid;
      border-color: #fce138;
      display: inline-block;  
  }
  .primary-border{
      border-color: #fce138;
  }
  .secondary-border {
    border-color: #39a6b2;
  }
  .steps div {
    margin-bottom: 80px;
  }
  .steps img {
    width: 15%;
    margin: 10px 0;
  }
  .steps h3{
      color:#024e76;
      font-size: 46px;
      margin-top: 10px;
  }
  .steps p{
      color:#39a6b2;
      font-size: 23px;
  }
  .steps span{
      font-size: 38px;
  }