from core.embeds import error, success
from disnake import Game
from disnake.ext.commands import Cog, group, slash_command


class Dev(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.devs = [135811207645888515, 821306636605718548]

    async def cog_check(self, ctx) -> bool:
        if not ctx.author.id in self.devs:
            await ctx.send(embed=error("You cannot use this command."))
            return False
        return True

    async def cog_slash_command_check(self, inter) -> bool:
        if not inter.author.id in self.devs:
            await inter.send(embed=error("You cannot use this command."))
            return False
        return True

    @group()
    async def dev(self, ctx):
        pass

    @slash_command(name="dev", guild_ids=[1028306608100483082, 1005601917466058792])
    async def dev_slash(self, ctx):
        pass

    @dev_slash.sub_command(name="status")
    async def dev_status(self, ctx, status):
        """
        Change status of the bot.
        """

        await self.bot.change_presence(activity=Game(name=status))
        await ctx.send(embed=success("Status changed successfully."))

    @dev.command()
    async def status(self, ctx, status):
        await self.dev_status(ctx, status)


def setup(bot):
    bot.add_cog(Dev(bot))
