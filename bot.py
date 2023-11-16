import discord
from discord.ext import commands

server_id = 1003939832768233482

pd_role = "pd"
ems_role =  "ems"

update_status = ["Discord id not found", "Role already exists", "Role Updated", "Error while updating role"]
        
def run_discord_bot(user_id, job):
    TOKEN = "MTE3NDM0Njk3MDYzNTE4NjIxNg.Gskz4r.E6XwKz4jSknGvSqzvEvhbpyJjm5ofhDMWVsoZ0"
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='!', intents=intents)
    isRoleUpdated = [0]
    @client.event
    async def on_ready():
        try: 
            users = (client.get_guild(server_id)).members
            for user in users:
                if(str(user.id) == str(user_id)):
                    role = discord.utils.get(user.guild.roles, name = pd_role if job == pd_role else ems_role)
                    for _role in user.roles:
                        if str(_role.name) == str(pd_role if job == pd_role else ems_role):
                            print(_role)
                            isRoleUpdated.pop()
                            isRoleUpdated.append(1)
                            break
                    if isRoleUpdated[0] != 1:
                        await user.add_roles(role)
                        isRoleUpdated.pop()
                        isRoleUpdated.append(2)
            await client.close()
        except Exception as e:
            isRoleUpdated.pop()
            isRoleUpdated.append(3)
            await client.close()
    client.run(TOKEN)
    if isRoleUpdated[0] == 0:
        return { "message":update_status[0], "code": 200 }
    elif isRoleUpdated[0] == 1:
        return { "message":update_status[1], "code": 200 }
    elif isRoleUpdated[0] == 2:
        return { "message":update_status[2], "code": 200 }
    else:
        return { "message":update_status[3], "code": 404 }
