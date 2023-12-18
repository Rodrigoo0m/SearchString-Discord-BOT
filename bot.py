import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio
import io

def search_in_file(file_path, query):
    # Tenta abrir e ler o arquivo especificado, procurando a consulta fornecida.
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        query = query.lower()
        results = [line.strip() for line in lines if query in line.lower()]
        return results
    except FileNotFoundError:
        # Retorna erro se o arquivo não for encontrado.
        return [f"Erro: Arquivo não encontrado. Verifique o caminho do arquivo: {file_path}"]
    except Exception as e:
        # Retorna um erro genérico em caso de exceções não esperadas.
        return [f"Erro inesperado ao ler o arquivo: {e}"]

class SearchView(View):
    # Classe para criar uma view interativa no Discord, permitindo pesquisas em arquivos.
    def __init__(self, file_paths, bot, author, channel):
        super().__init__(timeout=180)
        self.file_paths = file_paths
        self.bot = bot
        self.author = author
        self.channel = channel

    async def on_timeout(self):
        # Desativa os botões após o tempo limite.
        for item in self.children:
            item.disabled = True
        await self.channel.edit(view=self)

    async def interaction_check(self, interaction):
        # Verifica se o usuário interagindo é o autor do comando.
        return interaction.user == self.author

    async def wait_for_query(self, interaction, file_path):
        # Aguarda a entrada do usuário para a pesquisa.
        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel
        
        await interaction.response.send_message('Por favor, insira o que deseja pesquisar:', ephemeral=True)

        try:
            message = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await interaction.user.send('A pesquisa foi cancelada por inatividade.')
        else:
            results = search_in_file(file_path, message.content)
            response = "\n".join(results) if results else f"Nenhum resultado encontrado para '{message.content}'."
            await self.send_long_message(interaction.user, response)

    async def send_long_message(self, user, message):
        # Envia mensagens longas como arquivos se ultrapassarem o limite de caracteres do Discord.
        if len(message) <= 2000:
            await user.send(message)
        else:
            with io.StringIO(message) as file:
                file.name = "resultados.txt"
                file.seek(0)
                await user.send(file=discord.File(file, "resultados.txt"))

        # Fecha o canal após enviar os resultados.
        await self.channel.delete(reason="Envio de resultados concluído.")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='start')
async def start(ctx):
    # Comando para iniciar a função de pesquisa.
    channel_name = f"private-{ctx.author.id}"
    existing_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
    
    if existing_channel:
        await ctx.send(f"Você já tem um canal privado: {existing_channel.mention}")
        return

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        ctx.author: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await ctx.guild.create_text_channel(name=channel_name, overwrites=overwrites)

    await channel.send(f"Bem-vindo ao seu canal privado, {ctx.author.mention}!")

    embed = discord.Embed(title="O que deseja?", description="Escolha uma das opções de lookup abaixo.", color=0x3498db)
    
    file_paths = {
        # Caminhos dos arquivos para a pesquisa.
        'Nome database': 'Localização do Arquivo',
        'Nome database': 'Localização do Arquivo',
        'Nome database': 'Localização do Arquivo',
        'Nome database': 'Localização do Arquivo',
        'Nome database': 'Localização do Arquivo',
    }

    view = SearchView(file_paths, bot, ctx.author, channel)

    for label, file_path in file_paths.items():
        button = Button(label=label, style=discord.ButtonStyle.primary)
        async def button_callback(interaction, fp=file_path):
            # Callback para cada botão.
            await view.wait_for_query(interaction, fp)
        button.callback = button_callback
        view.add_item(button)

    await channel.send(embed=embed, view=view)

# Token do bot (substitua pelo seu token real).
bot.run('SEU_TOKEN_AQUI')
