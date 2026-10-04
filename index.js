const { Client, GatewayIntentBits } = require('discord.js');

// 初始化機器人與設定權限意圖
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
});

// 機器人上線成功的提示
client.once('ready', () => {
  console.log(`機器人已成功登入：${client.user.tag}`);
});

// 監聽群組訊息
client.on('messageCreate', async (message) => {
  // 忽略其他機器人發的訊息
  if (message.author.bot) return;

  // 當有人輸入 >ping 時，回應 pong
  if (message.content === '>ping') {
    await message.reply('pong');
  }
});

// 請把下方文字替換成您重新生成的最新 Token（記得保留兩邊的單引號）
client.login('MTU1NjE3OTMwMzIwMzM0ODUwMQ.GFqpzO.7YodpCbXD8kfngvZ5wMNL5H5xdSnVZwWjBY_ls');
