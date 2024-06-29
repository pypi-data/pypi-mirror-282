import geopandas as gpd
import time

# Default export path if none specified
OUT_PATH = r'soil_types_cleaned.shp'

def eliminatePolygons(gdf, minsize, out_path = OUT_PATH):
	"""
	Merge all polygons of an area less than the minsize (square meters) with the largest polygon it is in contact with
	gdf 	: geodataframe on which we want to run the filter
	minsize	: the minimum polygon size to be kept
	out_path: optional, the output path. default is the current directory

	returns : cleaned geodataframe
	"""

	start = time.time()
	

	# Convert to desired projection

	gdf_projected = gdf.to_crs(26917)

	# Compute polygon area

	gdf_projected['area'] = gdf_projected['geometry'].area

	gdf_projected = gdf_projected.sort_values(by = 'area', ascending = False)

	# Give new identifier to be used for merging

	gdf_projected.insert(0,'temp', range(0, len(gdf_projected)))

	
	# Pass 1
	gdf_cleaned = runFilter(gdf_projected, minsize)

	# Pass 2 -- Is it necessary?
	# gdf_cleaned = runFilter(gdf_cleaned, minsize)

	print('   ...' + str(len(gdf_projected) - len(gdf_cleaned)), 'polygons eliminated')


	# Export cleaned polygon

	gdf_cleaned.to_file(out_path, driver='ESRI Shapefile')

	end = time.time()

	print("   ...executed polygon elimination in " + str((end - start) * 10**3) + "ms")

	return gdf_cleaned


def runFilter(gdf_projected, minsize):
	"""
	Merging algorithm: Check contact of every polygon with each other and dissolve by largest touching polygon.
	This part could probably be done more efficiently as currently runs in O(n^2)
	But for current uses, should never have that many polygons where that would be an issue as this is used for soil types, so it's probably fine.
	"""

	gdf_projected = gdf_projected.rename(columns = {'Soil Type':'soil_type'})

	for polygon1 in gdf_projected.itertuples():
		# For each polygon

		if (polygon1.area < minsize):		
			max_touching = -10
			
			for polygon2 in gdf_projected.itertuples():
				
				if (polygon1.area < polygon2.area):
					
					if (polygon2.geometry.touches(polygon1.geometry)):
						
						if (polygon2.area > max_touching):
							
							gdf_projected._set_value(polygon1.Index, 'temp', polygon2.temp)
							gdf_projected._set_value(polygon1.Index, 'soil_type', polygon2.soil_type)
							max_touching = polygon2.area


	

	gdf_projected = gdf_projected.rename(columns = {'soil_type':'Soil Type'})

	gdf_cleaned = gdf_projected.dissolve(by = 'temp', as_index = False)

	gdf_cleaned['area'] = gdf_cleaned['geometry'].area


	return gdf_cleaned
