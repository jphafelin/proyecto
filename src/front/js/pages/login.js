import React, {useState} from "react";
export const Login = () => {
    const [email, setEmail]= useState("")
    const [password, setPassword]= useState("")
    const handleClick = () =>{

        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "email": email,
        "password": password
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };

        fetch("https://3001-jphafelin-rutgreen-a2181wyfwey.ws-eu92.gitpod.io/api/login", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
        
        //console.log(access_token) 
        setEmail("") 
        setPassword("")
    }

   console.log(email);
   console.log(password);

    return (
        <div className="wrapper">
            <form className="form-signin"onSubmit={handleClick}>
                <h2 className="form-signin-heading">Ingresar</h2>
                <input type="text" className="form-control" name="username" placeholder="Email"value={email} onChange={ (e)=> {setEmail(e.target.value)}} required="" autoFocus="" />
                <input type="password" className="form-control" name="password" placeholder="Contraseña"value={password} onChange={ (e)=> {setPassword(e.target.value)}} required="" />
                <button className="btn btn-lg btn-primary btn-block" type="submit">Ingresar</button>
            </form>
        </div>

    );
};