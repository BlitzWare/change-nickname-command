@client.command(pass_context=True)
@commands.has_permissions(manage_permissions=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'**Nickname was changed for {member.mention}**')
