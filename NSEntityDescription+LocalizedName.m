//
//  NSEntityDescription+LocalizedName.m
//
//  Created by Cameron Spickert on 4/8/11.
//

#import "NSEntityDescription+LocalizedName.h"

@implementation NSEntityDescription (LocalizedName)

@dynamic localizedName;

- (NSString *)localizedName {
	static NSString *const localizedNameKeyFormat = @"Entity/%@";
	NSString *localizedNameKey = [NSString stringWithFormat:localizedNameKeyFormat, [self name]];
	NSString *localizedName = [[[self managedObjectModel] localizationDictionary] objectForKey:localizedNameKey];
  if (localizedName) {
    return localizedName;
  }
  return [self name];
}

@end
