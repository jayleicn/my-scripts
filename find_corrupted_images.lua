-- This file helps to find images that will arise an error when loaded by image.load().
-- Jie Lei  
-- github@jayleicn

require 'image'
require 'xlua'

os.execute('find . -type f -name "*.JPEG"' .. ' > imgpath.tmp')
local handle = io.popen('cat imgpath.tmp | wc -l')
local img_num = handle:read('*a')
handle:close()
img_num = tonumber(img_num)
print(('Images in total: %d'):format(img_num))


local count = 0
local total = 0
for line in io.lines('imgpath.tmp') do
   local ok, img = pcall(image.load, line)
   if not ok then
      print('error: ' .. line)
      count = count + 1
   end
   total  = total + 1
   if (total % 2000 == 0) then xlua.progress(total, img_num) end
end

os.execute('rm -f imgpath.tmp')

print('\n')
print(('Found %d wrong images'):format(count))
print('Done.')
