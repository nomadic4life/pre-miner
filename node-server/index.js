require("dotenv").config();
const { server } = require("./api/server");
const port = process.env.PORT || 8000;
server.listen(port, () => {
  console.log(`\n --- Server Listening on port ${port}\n`);
});

// get request last proof every timed cycle
// if last proof changed update miners
// if new miner send miner last proof

// for each hash solved update hash table

// manage miner rewards in a que, next in que will get reward  and cycyle through que to evenly distrubute rewards for each hash solved

// manage each miner base proof starting point and update miner with new base proof  when range of proofs has been completed
