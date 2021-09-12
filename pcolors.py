end= '\33[0m'
class fg:
	black= '\33[30m'
	red= '\33[31m'
	green= '\33[32m'
	yellow= '\33[33m'
	blue= '\33[34m'
	violet= '\33[35m'
	lightblue = '\33[36m'
	white  = '\33[37m'
	grey = '\33[90m'
	red2= '\33[91m'
	green2= '\33[92m'
	yellow2= '\33[93m'
	blue2= '\33[94m'
	violet2= '\33[95m'
	lightblue2= '\33[96m'
	white2= '\33[97m'
class bg:
	white= '\33[7m'
	black= '\33[40m'
	red= '\33[41m'
	green= '\33[42m'
	yellow= '\33[43m'
	blue= '\33[44m'
	violet= '\33[45m'
	lightblue= '\33[46m'
	white= '\33[47m'
class styles:
	bold= '\33[1m'
	italic='\33[3m'
	underline= '\33[4m'
def colorize(text, fg=None, bg=None, styles=None, color_end=True):
	end= '\33[0m'
	if not color_end:
		end=''
	result=''
	if fg:
		result+=fg
	if bg:
		result+=bg
	if styles:
		styles=tuple(styles)
		for style in styles:
			result+=style
	result+=f'{text}{end}'
	return result
def cprint(text, fg=None, bg=None, styles=None, color_end=True, end='\n', flush=False):
	print(colorize(text, fg, bg, styles, color_end), end=end, flush=flush)
def percent(part, whole):
	percentage = 100 * float(part)/float(whole)
	return percentage
def progress(current, finish, fill='#', color=fg.blue2):
	progress=fill*current
	spaces=' '*(finish-current)
	print('\r['+color+progress+end+spaces+'] '+str(current)+' of '+str(finish), end='', flush=True)
def progress2(current, finish, fill='#', color=fg.blue2, prefix=''):
	progress=round(percent(current, finish), 2)
	spaces=' '*(int(finish-progress/2))
	print(f'\r{prefix}[{color}{fill*int(progress/2)}{end}{spaces}]{progress}%', end='', flush=True)