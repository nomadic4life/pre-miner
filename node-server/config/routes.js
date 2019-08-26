// const null = require("../customMiddleware");

const { queryProof } = require("../routes");

const root = async (req, res) => {
  res.send("sanity check");
};

module.exports = (server, router) => {
  server.use("/api", queryProof(router));
  server.get("/", root);
};
