# --------By @Midhun_xD---------#
# --------By @Midhun_xD---------#

from telethon import Button, custom, events, functions
import telethon

async def check(channel_id, event, bot):
    try:
            result = await bot(
                functions.channels.GetParticipantRequest(
                    channel=channel_id, user_id=event.sender_id
                )
            )
            if result.participant:
                return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False

# --------By @Midhun_xD---------#
# --------By @Midhun_xD---------#
