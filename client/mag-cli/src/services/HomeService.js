
import axios from 'axios'

export default class HomeService {

  static getNews () {
    axios.get('http://localhost:5000/home')
    .then(res => {
      return res
    })
    .catch(e => {
      return {'err': e}
    })
  }
}
