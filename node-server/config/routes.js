// const null = require("../customMiddleware");

const {} = require("../routes");

const root = async (req, res) => {
  res.send("sanity check");
};

module.exports = (server, router) => {
  server.get("/", root);
};
