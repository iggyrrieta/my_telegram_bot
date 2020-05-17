require 'telegram_bot'
token = '1155848028:AAEspUwS1k6slzkxB1PEC5V43ODFS-e2oHo'
bot = TelegramBot.new(token: token)

bot.get_updates(fail_silently: true) do |message|
    puts "@#{message.from.username}: #{message.text}"
    command = message.get_command_for(bot)
  
    message.reply do |reply|
      case command
      when /start/i
        reply.text = "Hola!, tenia ganas de hablar contigo. Prueba el comando /fisica"
      when /fisica/i
        reply.text = "Ja Ja Ja, #{message.from.first_name}. 🤖"
      else
        reply.text = "No entiendo que quieres decir con #{command.inspect} ..."
      end
      puts "Enviando #{reply.text.inspect} a @#{message.from.username}"
      reply.send_with(bot)
    end
  end