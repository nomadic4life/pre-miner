
const playerList = [];
const playerPointer = 0
const minerList = [];
let currentLastProof, prevLastProof, difficulty;

const getLastProof = (player_id) => {
  // request proof from server
  let url = "none"
  axios.get(url)
  .then( results => {
    if (results.proof !== currentLastProof) {
      prevLastProof = currentLastProof
      currentLastProof = results.proof
      difficulty = results.difficulty
    }
  })
  .catch(err => {
    console.log(err)
  })
}

const manageLastProofRequest = () => {
  // invoke this function every 10 seconds
  if (playerList.length > 0) {
    getLastProof(playerList[playerPointer++])
    playerPointer = playerPointer % playerList.length
  }
}


const addPlayer = async (req, res) => {
  // post
  const { player_id } = req.body
  playerList.push(player_id)
  res.send("player id added to player list");
};

const getMinerID = async (req, res) => {
  // get
  const minerId = minerList.length
  minerList.push(minerId)
  res.send(minerId);
};

const mineLastProof = async (req, res) => {
  // get last proof from server
  // get based on timer
  res.send("sanity check");
};

// const getLastProof = async (req, res) => {
//   // get last proof from server
//   // get based on timer
//   res.send("sanity check");
// };


module.exports = {};
