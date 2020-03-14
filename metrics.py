import sys
import psutil

class Sys_Info:
    def display_Info(self):
      for info in self._get_Info:
        print(info)
        
    @property
    def _get_Info(self):
        yield 'For get information you have to use parameters: cpu or mem'
        

class CPU_Info(Sys_Info):
    @property
    def _get_Info(self):
        try:
            cpu_time = psutil.cpu_times_percent(interval=1.0,percpu=False)
            yield 'system.cpu.idle   {}'.format(cpu_time.idle)
            yield 'system.cpu.user   {}'.format(cpu_time.user)
            yield 'system.cpu.guest  {}'.format(cpu_time.guest)
            yield 'system.cpu.iowait {}'.format(cpu_time.iowait)
            yield 'system.cpu.stolen {}'.format(cpu_time.steal)
            yield 'system.cpu.system {}'.format(cpu_time.system)
        except:
            yield 'CPU info ERROR'
            

class MEM_Info(Sys_Info):
    @property
    def _get_Info(self):
        try:
            virtual_mem = psutil.virtual_memory()
            yield 'virtual total  {}'.format(virtual_mem.total)
            yield 'virtual used   {}'.format(virtual_mem.used)
            yield 'virtual free   {}'.format(virtual_mem.free)
            yield 'virtual shared {}'.format(virtual_mem.shared)
        except:
            yield 'Virtual memory info ERROR'
        try:
            swap_mem = psutil.swap_memory()
            yield 'swap total {}'.format(swap_mem.total)
            yield 'swap used  {}'.format(swap_mem.used)
            yield 'swap free  {}'.format(swap_mem.free)
        except:
            yield 'Swap memory info ERROR'

__dict_info ={
    'cpu': CPU_Info(),
    'mem': MEM_Info()
}
 
def main(argv): 
    info = __dict_info.get(argv[0] if len(argv)==1 else '', Sys_Info()) 
    info.display_Info()

if __name__ == "__main__":
      main(sys.argv[1:]) 
