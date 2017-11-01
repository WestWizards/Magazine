import axios from 'axios'

export default class MagazineService {

  static getNumbersMag () {
    axios.get('http://localhost:5000/magazine')
    .then(res => {
      return res
    })
    .catch(e => {
      return {'err': e}
    })
  }
}
