import validator from 'validator'
import axios from 'axios'

// TODO : discuss about constructors, bind() and others class scope related
export default class AuthService {

  static login (data) {
    // TODO : use service (or utils) to globalize all validations in app
    axios.post('http://localhost:5000/login', data)
    .then(res => {
      console.log(res)
      localStorage.setItem('user', res)
      return {'success': 'Login success'}
      // TODO : redirect
    })
    .catch(e => {
      return {'err': e}
    })
    // return user and jwt
  }

  static logout () {
    // TODO : axios.post(/logout), delete jwt
  }

  static isAuth () {
    // TODO : do better
    if (localStorage.getItem('user') == null) {
      return false
    } else {
      return true
    }
  }

  validateData (data) {
    // Search and Discover : spread operator in switch case
    // TODO : add try catch
    if (data.username) {
      validator.isAlphanumeric(data.username)
      validator.escape(data.username)
    }
    if (data.password) {
      validator.isAlphanumeric(data.password)
      validator.escape(data.password)
    }
  }
}
