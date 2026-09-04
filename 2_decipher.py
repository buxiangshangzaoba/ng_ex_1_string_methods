encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

parts = encoded.split('|')
fragments = []

for p in parts:
    p = p.strip()
    if p.startswith('[') and p.endswith(']'):
        inner = p[1:-1]
        nums, text, status = inner.split('::')
        if status == 'ok' and nums.isdigit():
            fragments.append((int(nums), text))

decoded = {}

for num, text in fragments:
    res = ''
    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            res += alphabet[(idx - num) % 26]
        else:
            res += ch
    decoded[num] = res

msg = ''
for num in sorted(decoded.keys()):
    msg += decoded[num]

print(msg)