import { useState } from "react";
import { useNavigate} from "react-router-dom";

function Register() {
    const [email, setEmail] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [firstName, setfirstName] = useState('')
    const [lastName, setlastName] = useState('')
    const navigate = useNavigate()
    const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:8000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            email,
            username,
            password,
            first_name: firstName,
            last_name: lastName

        })
    })
        const data = await response.json()

    if (response.ok) {
        localStorage.setItem('token', data.access_token)
        navigate('/login')
    } else {
        alert(data.detail)
    }}
    return (  // ← return starts HERE, outside handleSubmit
        <div>
            <h2>Join HypeCheck</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="First Name" value={firstName} onChange={(e) => setfirstName(e.target.value)} />
                <input type="text" placeholder="Last Name" value={lastName} onChange={(e) => setlastName(e.target.value)} />
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Register</button>
            </form>
        </div>
    )
}

export default Register
