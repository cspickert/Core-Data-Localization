//
//  NSPropertyDescription+LocalizedName.m
//
//  Created by Cameron Spickert on 4/8/11.
//

#import "NSPropertyDescription+LocalizedName.h"

@implementation NSPropertyDescription (LocalizedName)

@dynamic localizedName;

- (NSString *)localizedName {
	static NSArray *localizedNameKeyFormats = nil;
	if (!localizedNameKeyFormats) {
		localizedNameKeyFormats = [[NSArray alloc] initWithObjects:@"Property/%@/Entity/%@", @"Property/%@", nil];
	}
	for (NSString *localizedNameKeyFormat in localizedNameKeyFormats) {
		NSString *localizedNameKey = [NSString stringWithFormat:localizedNameKeyFormat, [self name], [[self entity] name]];
		NSString *localizedName = [[[[self entity] managedObjectModel] localizationDictionary] objectForKey:localizedNameKey];
		if (localizedName) {
			return localizedName;
		}
	}
	return [self name];
}


@end
