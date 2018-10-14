import axios from 'axios'

let $backend = axios.create({
  baseURL: '/api',
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

// Response Interceptor to handle and log errors
$backend.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$backend.$fetchMessages = () => {
  return $backend.get(`stocks/`)
    .then(response => response.data)
}

$backend.$fetchMessage = (stockID) => {
  return $backend.get(`stocks/${stockID}`)
    .then(response => response.data)
}

$backend.$postMessage = (payload) => {
  return $backend.post(`stocks/`, payload)
    .then(response => response.data)
}

$backend.$updateMessage = (payload) => {
  return $backend.put(`stocks/${payload.pk}`, payload)
    .then(response => response.data)
}

$backend.$deleteMessage = (stockID) => {
  return $backend.delete(`stocks/${stockID}`)
    .then(response => response.data)
}

export default $backend