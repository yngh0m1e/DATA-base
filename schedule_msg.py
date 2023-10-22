from kodland_db import db
from discord.ext import commands, tasks
import discord

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.command('set')
async def set(ctx, task, minutes):
    db.tasks.put({'description': task,
                  'minutes': int(minutes),
                  'user_id': ctx.author.id})
    await ctx.send('Задача добавлена')

@tasks.loop(minutes=1)
async def called_once_a_minute():
    todo_tasks = db.tasks.get_all()
    for task in todo_tasks:
        task.minutes -= 1
        if task.minutes == 0:
            message_channel = await bot.fetch_user(task.user_id)
            await message_channel.send(task.description)
            db.tasks.delete('id', task.id)
        else:
            db.tasks.update('id', task.id, 'minutes', task.minutes)

called_once_a_minute.start()
bot.run('MTEzNTE1NDg')
