import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
	site: 'https://dev-docs.moodybeard.com',
	integrations: [
		starlight({
			title: 'dev-docs',
			head: [
				{
					tag: 'script',
					attrs: { type: 'application/ld+json' },
					content: JSON.stringify({
						'@context': 'https://schema.org',
						'@type': 'WebSite',
						name: 'dev-docs',
						url: 'https://dev-docs.moodybeard.com',
					}),
				},
			],
			locales: {
				root: { label: '한국어', lang: 'ko' },
				en: { label: 'English', lang: 'en' },
			},
			sidebar: [
				{
					label: 'Codex',
					translations: {
						en: 'Codex',
					},
					autogenerate: { directory: 'codex' },
				},
				{
					label: 'Next.js',
					translations: { en: 'Next.js' },
					autogenerate: { directory: 'nextjs' },
				},
			],
		}),
		sitemap(),
	],
});
