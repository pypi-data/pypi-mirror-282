import asyncio
import time
from multiprocessing import Pool

def calculate_pi_leibniz_sync(iterations):
	pi = 0
	sign = 1
	for i in range(iterations):
		term = sign * (1 / (2*i + 1))
		pi += term
		sign = -sign
	
	return pi * 4
	
async def calculate_pi_leibniz(iterations):
	pi = 0
	sign = 1
	for i in range(iterations):
		term = sign * (1 / (2*i + 1))
		pi += term
		sign = -sign	
	
	return pi * 4

async def main():
	boucles = int(input("Nombre de boucles : "))
	iterations = int(input("Nombre de d'itérations : "))
	print('début du traitement sychrone')
	start_time = time.time()
	for i in range(boucles):
		print(f'calcul {i + 1}', end='', flush=True)
		calculated_pi = calculate_pi_leibniz_sync(iterations)
		print(' fini')
		
	end_time = time.time()
	
	print(f'Valeur calculée de pi avec {iterations} itérations : {calculated_pi}')
	print(f"Temps d'execution : {end_time - start_time} secondes")
	print('Fin du traitement sychrone')
	
	print('début du traitement asychrone')
	start_time_async = time.time()
	tasks = []
	
	with Pool(boucles) as p:
		list_iterations = []
		for i in range(boucles):
			list_iterations.append(iterations)
		print(f'calcul async', end='', flush=True)
		result_async = p.map(calculate_pi_leibniz_sync, list_iterations)
		print(' fini')
	
	end_time_async = time.time()
	print(f'Valeur calculée de pi avec {iterations} itérations : {result_async}')
	print(f"Temps d'execution : {end_time_async - start_time_async} secondes")
	print('Fin du traitement asychrone')
	
		
	print('fini')
	
if __name__ == "__main__":
	asyncio.run(main())

